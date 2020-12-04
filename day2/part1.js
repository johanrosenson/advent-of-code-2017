// run in browser console on input page

(function (rows) {
    var cs = 0;
    for(var i = 0, imax = rows.length; i < imax; i++) {
        var numbers = rows[i].match(/[^\s]+/g);
        var min = null;
        var max = null;
        for(var j = 0, jmax = numbers.length; j < jmax; j++) {
            min = Math.min(min !== null ? min : numbers[j], numbers[j]);
            max = Math.max(max !== null ? max : numbers[j], numbers[j]);
        }
        cs = cs + (max - min);
    }
    return cs;
})(document.body.innerText.match(/[^\r\n]+/g));
