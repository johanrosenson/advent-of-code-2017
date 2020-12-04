// run in browser console on input page

(function (rows) {
    var cs = 0;
    for(var i = 0, imax = rows.length; i < imax; i++) {
        var numbers = rows[i].match(/[^\s]+/g);
        var result = 0;
        for(var j = 0, jmax = numbers.length; j < jmax; j++) {
            for(var k = 0, kmax = numbers.length; k < kmax; k++) {
                if(numbers[k] != numbers[j] && !(numbers[k] % numbers[j])) {
                    result = numbers[k] / numbers[j];
                    break;
                }
            }
            if(result) {
                break;
            }
        }
        cs = cs + result;
    }
    return cs;
})(document.body.innerText.match(/[^\r\n]+/g));
