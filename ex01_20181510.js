const myFunction = function(n, k){
    var result = 0;
    if(k == null){
        k = 2;
    };
    if(n < 1 || k < 1){
        return console.log("조건을 만족하지 않습니다.");
    } else {
        for(var i = 1; i <= n; i++){
            if(i % k == 0){
                result += i;
            };
        };
    };
    return console.log(result)
};

myFunction(100, 5);
