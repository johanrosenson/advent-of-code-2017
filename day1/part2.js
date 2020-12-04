// run in browser console on input page

(function (numbers) {
    var cs = 0;
    for(var i = 0, imax = numbers.length; i < imax; i++) {
        let current = Number(numbers[i]);
        let next = Number((i+numbers.length/2) < numbers.length ? numbers[i+numbers.length/2] : numbers[(i + numbers.length/2) - numbers.length]);
        if(current == next) {
            cs = cs + current;
        }
    }
    return cs;
})(document.body.innerText.match(/[\d]/g));
