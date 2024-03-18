
// this event listener, listens for when the view port is looking at the num ,then increments it for funsys
// the incrementing tp 60  VVVV
document.addEventListener('scroll', function () {
    var targetSection = document.getElementById('numElement');
    var rect = targetSection.getBoundingClientRect();

    if (rect.top <= window.innerHeight && rect.bottom >= 0) { //makes sure your at the right spot
        if (targetSection.innerHTML == '0'){                //validation
            for (var i = 1; i <= 60; i++) {                 //number params
                (function (currentValue) {                  //a closure to capture the current value of i //note this is to ensure the for loop increments slower 
                    setTimeout(function () {                //delay so every change perceptible 
                        targetSection.innerHTML = currentValue.toString();
                    }, i * 50);
                })(i);
            }
        }
    }
});

// the incrementing to 11  VVVV
document.addEventListener('scroll', function () {
    var targetSection = document.getElementById('numElement2');
    var rect = targetSection.getBoundingClientRect();

    if (rect.top <= window.innerHeight && rect.bottom >= 0) { //makes sure your at the right spot
        if (targetSection.innerHTML == '0'){                //validation
            for (var i = 1; i <= 11; i++) {                 //number params
                (function (currentValue) {                  //a closure to capture the current value of i //note this is to ensure the for loop increments slower 
                    setTimeout(function () {                //delay so every change perceptible 
                        targetSection.innerHTML = currentValue.toString();
                    }, i * 100);
                })(i);
            }
        }
    }
});

// this controls the mobile view of the careers accordion, contact form div
window.addEventListener('resize', function () {
    var contactElement = document.getElementById('contactForm');
    if (window.innerWidth <= 768) {
        contactElement.classList.remove('w-50');
        contactElement.classList.add('w-75');
    } else {
        contactElement.classList.add('w-50');
        contactElement.classList.remove('w-75');
    }
});

// this controls the mobile view of the contact form div
window.addEventListener('resize', function () {
    var accordionElement = document.getElementById('benefitsAccordion');
    if (window.innerWidth <= 768) {
        accordionElement.classList.remove('w-50');
    } else {
        accordionElement.classList.add('w-50');
    }
});

