/**
 * Created by Gatsby on 2/11/2017.
 */
app.controller('myCtrl', function($scope, $http) {
    $rootScope.$on('keypress', function (e, a, key) {
        $scope.$apply(function () {
            $scope.key_code = key;
        });
    })

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

    $scope.nextPage = function(page){
        $scope.image_page = page + 1;
        $http({
            method: 'GET',
            url: urlfield+ 'db/' + database + '/' +  $scope.orderSelection + '/' + $scope.image_page + '/'
        }).then(function successCallback(response) {
            datatoarray($scope, response.data);
            console.log(response);
        }, function errorCallback(response) {
            console.log(response)
            // called asynchronously if an error occurs
            // or server returns response with an error status.
        });

    };

    $scope.prevPage = function(page){
        $scope.image_page = page - 1;
        $http({
            method: 'GET',
            url: urlfield+ 'db/' + database + '/' + $scope.orderSelection + '/' + $scope.image_page + '/'
        }).then(function successCallback(response) {
            datatoarray($scope, response.data);
            console.log(response);
        }, function errorCallback(response) {
            console.log(response)
            // called asynchronously if an error occurs
            // or server returns response with an error status.
        });


    };
    var datatoarray = function(scope, data){
        for (var i = 0; i < data.length; i++) {
            scope.imageUrlArray[(i*4)] = 'images/gd1' + data[i]['url_orig'];
            scope.imageUrlArray[(i*4)+1] = 'images/gd1' + data[i]['url_pos'];
            scope.imageUrlArray[(i*4)+2] = 'images/gd1' + data[i]['url_neg'];
            scope.imageUrlArray[(i*4)+3] = 'images/gd1' + data[i]['url_hot'];
        };
    }

    var init = function(){
        $scope.orders = ["correct", "incorrect"];
        $scope.orderSelection = "incorrect"
        $scope.image_page = 0;
        $http({
            method: 'GET',
            url: urlfield+ 'db/' + database + '/' +  $scope.orderSelection + '/' + $scope.image_page + '/'
        }).then(function successCallback(response) {
            datatoarray($scope, response.data);
            console.log(response);
        }, function errorCallback(response) {
            console.log(response);
            // called asynchronously if an error occurs
            // or server returns response with an error status.
        });

    };
    var urlfield = 'http://127.0.0.1:8000/'
    var correctness = 'correct'
    var database = 'SUN397'

    init();
});
