// run in browser console on input page

(function (rows) {
    var valid = 0;
    for(var i = 0, imax = rows.length; i < imax; i++) {
        if(!rows[i].match(/(?:(?:^|\s)([^\s]+))(?=\s.*\1(\s|$))/g)) {
            valid++;
        }
    }
    return valid;
})(document.body.innerText.match(/[^\r\n]+/g));
