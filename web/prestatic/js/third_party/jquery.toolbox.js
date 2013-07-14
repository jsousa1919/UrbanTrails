(function (site) {
    site.widget("custom.tool", {
        _create: function () {
            // set up options
            var self = this,
                image_class = this.options.image_class,
                input_id = image_class + "-input",
                text = this.options.text;
            this.workspace = this.options.workspace;

            // set up DOM elements
            this.input =
                site("<input type='radio' />")
                .attr("name", this.options.group)
                .attr("id", input_id)
                .hide();

            this.label = site("<label></label>")
                .attr("for", input_id)
                .text(text);

            this.element
                .empty()
                .append(this.label)
                .append(this.input)
                .addClass("tool")
                .removeAttr("name");

            if (this.options.default === true) {
                this._select();
            }

            // use jquery ui button widget
            this.input.button({
                icons: {
                    primary: image_class
                },
                text: false
            });

            // let the workspace know the currently selected tool
            this._on(this.element, {
                click: "_select"
            });

            // set up listeners for each type of event this tool uses
            if (this.options.dom_events !== undefined) {
                site.each(self.options.dom_events, function (event, f) {
                    self.workspace.workspace('request_dom_event', event);
                });
            }
            if (this.options.map_events !== undefined) {
                site.each(self.options.map_events, function (event, f) {
                    self.workspace.workspace('request_map_event', event);
                });
            }
        },
        _select: function () {
            // called when tool is selected
            // lets workspace know which tool gets the event
            this.input.prop('checked', true);
            this.workspace.workspace('set_tool', this)
        },
        trigger: function (type, event, e) {
            // workspace is triggering an event and this tool is selected
            // different tools may listen for different events, so check if the tool handles the triggered event
            if (type in this.options && event in this.options[type]) {
                this.options[type][event](e);
            }
        }
    });

    site.widget("custom.workspace", {
        _create: function () {
            this.dom_events = [];
            this.map_events = [];
            this.map = this.options.map;
        },
        set_tool: function (tool) {
            // a tool has been selected
            this.current_tool = tool;
        },
        request_dom_event: function (event) {
            // tool has a dom event to listen for
            var self = this,
                tmp = {};

            // make sure every type of event only gets one listener
            // we don't want things firing multiple times
            if (site.inArray(event, this.dom_events) === -1) {
                this.dom_events.push(event);

                // when an event of this type happens, try to call it for the current tool
                // slight hack to use jquery ui widgets event handling
                tmp[event_name] = function (e) {
                    if (self.current_tool !== undefined) {
                        self.current_tool.trigger('dom_events', event, e);
                    }
                };
                this._on(tmp);
            }
        },
        request_map_event: function (event) {
            // tool has a google map event to listen for
            var self = this;

            // make sure every type of event only gets one listener
            // we don't want things firing multiple times
            if (site.inArray(event, this.map_events) === -1) {
                this.map_events.push(event);


                // when an event of this type happens, try to call it for the current tool
                google.maps.event.addListener(this.map, event, function (e) {
                    if (self.current_tool !== undefined) {
                        self.current_tool.trigger('map_events', event, e);
                    }
                });
            }
        }
    })
}(jQuery));