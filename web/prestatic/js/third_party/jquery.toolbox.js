(function (site) {
    site.widget("custom.tool", {
        _create: function () {
            var self = this,
                name = this.element.attr("name"),
                id = this.element.attr("id"),
                input_id = id + "-input",
                text = this.element.text();

            this.input =
                site("<input type='radio' />")
                .attr("name", name)
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

            this.input.button({
                icons: {
                    primary: id
                },
                text: false
            });

            this.workspace = site(this.options.workspace).workspace({
                map: this.options.map
            });

            this._on(this.element, {
                click: "_select"
            });

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
            this.input.prop('checked', true);
            this.workspace.workspace('set_tool', this)
        },
        trigger: function (type, event, e) {
            this.options[type][event](e)
        }
    });

    site.widget("custom.workspace", {
        _create: function () {
            if (!this.element.hasClass("_workspace")) {
                this.element.addClass("_workspace");

                this.dom_events = [];
                this.map_events = [];
            }
        },
        set_tool: function (tool) {
            this.current_tool = tool;
        },
        request_dom_event: function (event) {
            var self = this,
                tmp;
            if (site.inArray(event, this.dom_events) === -1) {
                this.dom_events.push(event);
                tmp = {};
                tmp[event_name] = function (e) {
                    if (self.current_tool !== undefined) {
                        self.current_tool.trigger('dom_events', event, e);
                    }
                };
                this._on(tmp);
            }
        },
        request_map_event: function (event) {
            var self = this;
            if (site.inArray(event, this.map_events) === -1) {
                this.map_events.push(event);
                google.maps.event.addListener(this.options.map, event, function (e) {
                    if (self.current_tool !== undefined) {
                        self.current_tool.trigger('map_events', event, e);
                    }
                });
            }
        }
    })
}(jQuery));