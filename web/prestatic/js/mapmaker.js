(function (site) {
    "use strict";

    var priv = new (function () {
            this.suggestWindow = function suggestWindow(latLng, suggestions) {
                var container = site("#suggest-window"),
                    listings = container.find(".suggestion"),
                    template = listings.first(),
                    add_button = container.find(".add_button"),
                    options = {
                        position: latLng
                    };

                site.maps.infoWindow.setOptions(options);
                listings.slice(suggestions.length).remove();

                site.each(suggestions, function (i, suggestion) {
                    var listing;
                    if (i >= listings.length) {
                        listing = template.clone();
                        add_button.before(listing);
                    } else {
                        listing = listings.slice(i, i + 1);
                    }

                    listing.find(".image").attr("src", suggestion.icon);
                    listing.find(".name").text(suggestion.name);
                    listing.find(".address").text(suggestion.vicinity);
                });

                site("#suggest-window .suggestion").hide();
                listings.slice(0, 3).show();
                site.maps.infoWindow.setContent(container.html());
                site.maps.infoWindow.open(site.maps.map);
            };
        })(),
        pub = {
            searchNearby: function searchNearby(latLng) {
                var parameters = {
                    location: latLng,
                    radius: 100,
                    types: site.maps.userPoiTypes
                };
                site.maps.places.nearbySearch(parameters, function (results, status) {
                    if (status === google.maps.places.PlacesServiceStatus.OK) {
                        priv.suggestWindow(latLng, results);
                    } else {
                        console.log("Nearby search failed due to: " + status);
                    }
                });
            },
            showSuggestionsPage: function showSuggestionPage(i) {
                var listings = site("#suggest-window .suggestion");
                listings.hide();
                listings.slice(i * 3, (i * 3) + 3).show();
            }
        },
        events = function () {
            google.maps.event.addListener(site.maps.map, 'click', function (event) {
                site.maps.clickTimeout = setTimeout(function () {
                    site(".tool input:checked").parent().tool("fire", 'click', event);
                }, 200);
            });
            google.maps.event.addListener(site.maps.map, 'dblclick', function () {
                clearTimeout(site.maps.clickTimeout);
            });
            site("#line").tool();
            site("#cursor").tool();
            site("#spyglass").tool({
                click: function (event) {
                    site.maps.searchNearby(event.latLng);
                }
            });
        };
    site.extend(site.maps, pub);
    site.events.mapmaker = events;

    site.widget("custom.tool", {
        _create: function () {
            this.label = site("<label></label>")
                .attr("for", this.element.attr("id"))
                .text(this.element.text());

            this.input = site("<input type='radio' />")
                .attr("id", this.element.attr("id"))
                .attr("name", "radio");

            this.element.empty();
            this.element.append(this.label);
            this.element.append(this.input);

            if (this.element.data("default") === true) {
                this.input.prop("checked", true);
            }

            this.input.button({
                icons: {
                    primary: this.element.attr('class')
                },
                text: false
            });
            this.element.removeClass();
            this.element.addClass("tool");

            this._on(this.label, {
                click: "_select"
            })
        },
        _select: function () {
            this.input.prop('checked', true);
        },
        fire: function (type, event) {
            (this.options[type] || function () {})(event);
        }
    })
}(site));