(function (site) {
    site.widget("custom.tool", {
        _create: function () {
            var self = this,
                name = this.element.attr("name");

            this.input =
                site("<input type='radio' />")
                .attr("name", name)
                .hide();

            this.element.after(this.input);
            this.workspace = site(this.options.workspace).workspace();

            this._on(this.element, {
                click: "_select"
            });

            site.each(self.options, function (event, f) {
                if (site.inArray(event, ['create', 'disabled', 'workspace']) === -1) {
                    self.workspace.workspace('request', event);
                }
            });

        },
        _select: function () {
            this.input.prop('checked', true);
            this.workspace.workspace('set_tool', this)
        },
        trigger: function (event, e) {
            if (event in this.options) {
                this.options[event](e)
            }
        }
    });

    site.widget("custom.workspace", {
        _create: function () {
            if (!this.element.hasClass("_workspace")) {
                this.element.addClass("_workspace");

                this.events = [];
            }
        },
        set_tool: function (tool) {
            this.current_tool = tool;
        },
        request: function (event) {
            var self = this,
                tmp;
            if (site.inArray(event, this.events) === -1) {
                this.events.push(event);
                tmp = {};
                tmp[event] = function (e) {
                    if (self.current_tool !== undefined) {
                        self.current_tool.trigger(event, e);
                    }
                };
                this._on(tmp);
            }
        }
    })
}(jQuery));