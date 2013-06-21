(function (jQuery) {
    "use strict";
    var site = jQuery.noConflict(true);
    site.fx.interval = 24; //24fps (This is what movies run at so it's good enough for the site

    if (!window.site) {
        window.site = site;
    }

    site(document).unload(function () {
        site('*').off().removeData();
        window.site = null;
    });

    site.extend({
        common: {},
        maps: {},
        events: {},
        console: {
            assert: function () {},
            clear: function () {},
            count: function () {},
            debug: function () {},
            dir: function () {},
            dirxml: function () {},
            error: function () {},
            exception: function () {},
            group: function () {},
            groupCollapsed: function () {},
            groupEnd: function () {},
            info: function () {},
            log: function () {},
            memoryProfile: function () {},
            memoryProfileEnd: function () {},
            profile: function () {},
            profileEnd: function () {},
            table: function () {},
            time: function () {},
            timeEnd: function () {},
            timeStamp: function () {},
            trace: function () {},
            warn: function () {}
        }
    });

    if (!window.console) {
        window.console = site.console;
    }
}(jQuery));