const predictionForm = $("#predictionForm")[0];
const predictionSection = $("#predictionSection")[0];
const predictionResult = $("#predictionResult")[0];
const predictionPercentage = $("#predictionPercentage")[0];
const predictAgain = $("#predictAgain")[0];

// Get all input fields
const lat = $("#lat")[0];
const long = $("#long")[0];
const bright = $("#bright")[0];
const frp = $("#frp")[0];
const time =$("#time")[0];
const sat =$("#sat")[0];
const forest =$("#forest")[0];
const ind =$("#ind")[0];
const area =$("#area")[0];
const day =$("#day")[0];
const month =$("#month")[0];
const year =$("#year")[0];

$(predictionResult).hide();

// const API_ENDPOINT = "http://127.0.0.1:8000/predict";

async function predict(body) {
    // const config = {
    //     // method:"POST",
    //     body:JSON.stringify(body)
    // }
    const API_ENDPOINT = `http://127.0.0.1:8000/predict?latitude=${lat.value}&longitude=${long.value}&brightness=${bright.value}&satellite=${sat.value}&frp=${frp.value}&daynight=${time.value}&type_2=${forest.value}&type_3=${ind.value}&scan_binned=${area.value}&year=${year.value}&month=${month.value}&day=${day.value}`
    const apiResponse = await fetch(API_ENDPOINT);
    const response = await apiResponse.json();
    return response;
}

async function submitHandler(e) {
    e.preventDefault();
    const body = {
        lat: lat.value,
        long: long.value,
        bright: bright.value,
        frp: frp.value,
        time: time.value,
        sat: sat.value,
        forest: forest.value,
        ind: ind.value,
        area: area.value,
        day: day.value,
        month: month.value,
        year: year.value
    }
    // console.log(lat,lat.value)
    // const response = await predict(body);
    const API_ENDPOINT = `http://127.0.0.1:8000/predict?latitude=${lat.value}&longitude=${long.value}&brightness=${bright.value}&satellite=${sat.value}&frp=${frp.value}&daynight=${time.value}&type_2=${forest.value}&type_3=${ind.value}&scan_binned=${area.value}&year=${year.value}&month=${month.value}&day=${day.value}`
    const apiResponse = await fetch(API_ENDPOINT);
    let response = await apiResponse.json();
    $(predictionSection).hide();
    response = JSON.parse(response)[0].toFixed(2)
    console.log(response)
    $(predictionResult).show();
    $('html, body').animate({
        scrollTop: $(".breadcrumb").offset().top
    }, 500);
    setPercentage(response);
    $(predictionPercentage).text(`${response}%`)
}

function resetPredict() {
    $(predictionResult).hide();
    $(predictionSection).show();
    $(predictionForm).trigger("reset");
}

predictionForm.addEventListener("submit",submitHandler);

predictAgain.addEventListener("click",resetPredict)

var forEach = function (array, callback, scope) {
	for (var i = 0; i < array.length; i++) {
		callback.call(scope, i, array[i]);
	}
};
function setPercentage(percent){
	var max = -219.99078369140625;
	forEach(document.querySelectorAll('.progress'), function (index, value) {
		value.querySelector('.fill').setAttribute('style', 'stroke-dashoffset: ' + ((100 - percent) / 100) * max);
		value.querySelector('.value').innerHTML = percent + '%';
	});
}