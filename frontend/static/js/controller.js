/**
 * Created by Gatsby on 2/11/2017.
 */
app.controller('myCtrl', function($scope, $http) {
    $scope.orders = ["alphabet", "lament"];



    $scope.range = function(min, max, step) {
        step = step || 1;
        max = max || -1;
        if (min > max){
            max = min;
            min = 0;
        }
        var input = [];
        for (var i = min; i < max; i += step) {
            input.push(i);
        }
        return input;
    };

    $scope.myImage = function(){
        var i = 0;
        if (i == 0) {
            console.log(0)
            return "images/photos/sun_aaaulhwrhqgejnyt-orient2.jpg";
        } else {
            console.log(1)
            return "images/photos/sun_aaaulhwrhqgejnyt-prob0-orient2-pred2-cw.jpg";
        }
    }

    $scope.nextPage = function(page, order){
        $scope.imageUrlArray = ["images/photos/sun_aaaulhwrhqgejnyt-prob0-orient2-pred2-cw.jpg", "images/photos/sun_aaaulhwrhqgejnyt-orient2.jpg", "images/photos/sun_aaaulhwrhqgejnyt-prob0-orient2-pred2-cw.jpg", "images/photos/sun_aaaulhwrhqgejnyt-orient2.jpg", "images/photos/sun_aaaulhwrhqgejnyt-prob0-orient2-pred2-cw.jpg", "images/photos/sun_aaaulhwrhqgejnyt-orient2.jpg", "images/photos/sun_aaaulhwrhqgejnyt-prob0-orient2-pred2-cw.jpg", "images/photos/sun_aaaulhwrhqgejnyt-orient2.jpg", "images/photos/sun_aaaulhwrhqgejnyt-prob0-orient2-pred2-cw.jpg", "images/photos/sun_aaaulhwrhqgejnyt-orient2.jpg", "images/photos/sun_aaaulhwrhqgejnyt-prob0-orient2-pred2-cw.jpg", "images/photos/sun_aaaulhwrhqgejnyt-orient2.jpg", "images/photos/sun_aaaulhwrhqgejnyt-prob0-orient2-pred2-cw.jpg"];
        app.directive("imageSource");
        $scope.image_page = page + 1;
    };
    $scope.prevPage = function(page, order){
        $scope.imageUrlArray = ["images/photos/sun_aaaulhwrhqgejnyt-orient2.jpg", "images/photos/sun_aaaulhwrhqgejnyt-prob0-orient2-pred2-cw.jpg", "images/photos/sun_aaaulhwrhqgejnyt-orient2.jpg", "images/photos/sun_aaaulhwrhqgejnyt-prob0-orient2-pred2-cw.jpg", "images/photos/sun_aaaulhwrhqgejnyt-orient2.jpg", "images/photos/sun_aaaulhwrhqgejnyt-prob0-orient2-pred2-cw.jpg", "images/photos/sun_aaaulhwrhqgejnyt-orient2.jpg", "images/photos/sun_aaaulhwrhqgejnyt-prob0-orient2-pred2-cw.jpg", "images/photos/sun_aaaulhwrhqgejnyt-orient2.jpg", "images/photos/sun_aaaulhwrhqgejnyt-prob0-orient2-pred2-cw.jpg", "images/photos/sun_aaaulhwrhqgejnyt-orient2.jpg", "images/photos/sun_aaaulhwrhqgejnyt-prob0-orient2-pred2-cw.jpg", "images/photos/sun_aaaulhwrhqgejnyt-orient2.jpg", "images/photos/sun_aaaulhwrhqgejnyt-prob0-orient2-pred2-cw.jpg"]
        $scope.image_page = page - 1;
    };
});