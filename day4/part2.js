// run in browser console on input page

(function (rows) {
    var valid = 0;
    for(var i = 0, imax = rows.length; i < imax; i++) {
        let words = rows[i].match(/[^\s]+/g);
        var hashes = {};
        var hash_found = false;
        for(var j = 0, jmax = words.length; j < jmax; j++) {
            var hash = words[j].split('').sort().join('');
            if(hashes[hash]) {
                hash_found = true;
                break;
            }
            hashes[hash] = 1;
        }
        if(!hash_found) {
            valid++;
        }
    }
    return valid;
})(document.body.innerText.match(/[^\r\n]+/g));
