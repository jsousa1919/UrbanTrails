(function (site) {
    "use strict";
    var priv = new (function () {
            this.googleApiKey = "AIzaSyClW-y8gcnOv5QgRHJ-CqUS6iU0VXhMVF4";
            this.mapOptions = {
                styles: [
                    {
                        stylers: [
                            { hue: "#00ffe6" },
                            { saturation: -20 }
                        ]
                    }, {
                        featureType: "road",
                        elementType: "geometry",
                        stylers: [
                            { lightness: 100 },
                            { visibility: "simplified" }
                        ]
                    }, {
                        featureType: "road",
                        elementType: "labels",
                        stylers: [
                            { visibility: "off" }
                        ]
                    }, {
                        featureType: "poi",
                        elementType: "labels",
                        stylers: [
                            { visibility: "on" }
                        ]
                    }
                ]
            };
            this.defaultMapOptions = site.extend(site.common.clone(this.mapOptions), {
                center: new google.maps.LatLng(40.7142, -74.0064),
                zoom: 12,
                minZoom: 3,
                mapTypeId: google.maps.MapTypeId.HYBRID,
                mapTypeControl: false,
                scaleControl: false,
                zoomControl: false,
                streetViewControl: false,
                panControl: false
            });
            this.setMapStyle = function setMapStyle(property, value, featureType, elementType) {
                function setStyle(featureType, elementType, property, value) {
                    var styleFound = false,
                        newStyle,
                        newProperty;

                    function setStyler(selectedStyle, property, value) {
                        var propertyFound = false,
                            newProperty;
                        site.each(selectedStyle.stylers, function (j, style) {
                            if (style[property] !== undefined) {
                                propertyFound = true;
                                selectedStyle.stylers[j][property] = value;
                            }
                        });
                        if (!propertyFound) {
                            newProperty = {};
                            newProperty[property] = value;
                            selectedStyle.stylers.push(newProperty);
                        }
                    }

                    site.each(priv.mapOptions.styles, function (i, style) {
                        var selectedStyle;
                        if (style.featureType === featureType && style.elementType === elementType) {
                            selectedStyle = priv.mapOptions.styles[i];
                            styleFound = true;

                            if (selectedStyle.stylers === undefined) {
                                newProperty = [{}];
                                newProperty[0][property] = value;
                                selectedStyle.stylers = newProperty;
                            } else {
                                setStyler(selectedStyle, property, value);
                            }
                        }
                    });

                    if (!styleFound) {
                        newProperty = [{}];
                        newProperty[property] = value;

                        newStyle = {};
                        newStyle.featureType = featureType;
                        newStyle.elementType = elementType;
                        newStyle.stylers = newProperty;
                        priv.mapOptions.styles.push(newStyle);
                    }
                }

                setStyle(featureType, elementType, property, value);
                site.maps.map.setOptions(this.mapOptions);
            };
        })(),
        pub = {
            // FIXME: inputs from backend
            userPoiTypes: ["restaurant", "museum"],

            toggleRoadLabels: function toggleRoadLabels() {
                var onoff = site(this).is(":checked") ? "on" : "off";
                priv.setMapStyle("visibility", onoff, "road", "labels");
            },
            togglePoiLabels: function togglePoiLabels() {
                var onoff = site(this).is(":checked") ? "on" : "off";
                priv.setMapStyle("visibility", onoff, "poi", "labels");
            },
            poiDetails: function poiDetails(reference) {
                var parameters = {
                    reference: reference
                };
                site.maps.places.getDetails(parameters, function (place, status) {
                    if (status === google.maps.places.PlacesServiceStatus.OK) {
                        console.log(JSON.stringify(place));
                    } else {
                        console.log("Place details failed due to: " + status);
                    }
                });
            }
        },
        events = function () {
            site.maps.map_container = site("#map_canvas");
            site.maps.map = new google.maps.Map(site.maps.map_container[0], priv.defaultMapOptions);
            site.maps.places = new google.maps.places.PlacesService(site.maps.map);
            site.maps.infoWindow = new google.maps.InfoWindow();

            site("body").on("click", "#toggle-road-labels", pub.toggleRoadLabels);
            site("body").on("click", "#toggle-poi-labels", pub.togglePoiLabels);
        };
    site.extend(site.maps, pub);
    site.events.map = events;
}(site));