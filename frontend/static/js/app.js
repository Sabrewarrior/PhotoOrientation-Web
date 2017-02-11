/**
 * Created by Gatsby on 2/11/2017.
 */
var app = angular.module('myApp', [], function($interpolateProvider) {
    $interpolateProvider.startSymbol('{[{');
    $interpolateProvider.endSymbol('}]}');
});

app.directive("imageSource", function() {
    return { link: function (scope, element, attrs){
        console.log("page: " + scope.image_page + "\norder: " + scope.ordering);
        element.attr("src", scope.imageUrlArray[attrs.imageSource]);

    }
    };
});