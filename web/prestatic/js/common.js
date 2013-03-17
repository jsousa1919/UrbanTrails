(function (site) {
    "use strict";
    var priv = {

    }, pub = {
        urls: {},
        clone: function clone(obj) {
            var cl = {};
            site.extend(cl, obj);
            return cl;
        }
    };
    site.extend(site.common, pub);
}(site));