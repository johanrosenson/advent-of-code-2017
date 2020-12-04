// run in browser console on input page

(function (numbers) {
    var cs = 0;
    for(var i = 0, imax = numbers.length; i < imax; i++) {
        let current = Number(numbers[i]);
        let next = Number((i+1) < numbers.length ? numbers[i+1] : numbers[0]);
        if(current == next) {
            cs += current;
        }
    }
    return cs;
})(document.body.innerText.match(/[\d]/g));
