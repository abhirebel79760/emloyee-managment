$(document).ready(function () {
	$('.slider').slick({
		centerPadding: '60px',
		autoplay: true,
		arrows: false,
		responsive: [
			{
				breakpoint: 1024,
				settings: {
					slidesToShow: 2,
					slidesToScroll: 1,
				},
			},
			{
				breakpoint: 800,
				settings: {
					slidesToShow: 1,
					slidesToScroll: 1,
				},
			},
		],
	});
});
$(document).ready(function () {
	$('.top').slick({
		dots: false,
		infinite: true,
		speed: 200,
		slidesToShow: 1,
		autoplay: true,
		arrows: true,
		cssEase: 'linear',
	});
});

$('.youtuber-left ').click(function () {
	$('.slider').slick('slickPrev');
});

$('.youtuber-right').click(function () {
	$('.slider').slick('slickNext');
});

$('.team-left ').click(function () {
	$('.slider').slick('slickPrev');
});

$('.team-right').click(function () {
	$('.slider').slick('slickNext');
});




const td = document.querySelector(".date")
const dv = document.querySelector(".hi")
const status = document.querySelector(".status")
let checked = document.querySelector(".checked")
let update = document.querySelector(".update")

let subDate = update.innerText
console.log(subDate)
let date = subDate.slice(0, 19)
console.log(`after splice ${date}`)

if (subDate) {

	update.innerText = (date)
}

if (subDate == "False") {
	update.innerText = "Not update yet"
}





let today = new Date();
const dd = String(today.getDate()).padStart(2, '0');
const mm = String(today.getMonth() + 1).padStart(2, '0'); //January is 0!
const yyyy = today.getFullYear();

today = yyyy + '-' + mm + '-' + dd;

let finalSatus = (status.innerText).toUpperCase()

let checkedValue = checked.innerText

let text = td.innerText
console.log(text)
console.log(finalSatus)
console.log(checkedValue)
if (today > text) {
	if (finalSatus === "COMPLETED" && checkedValue === "True") {
		dv.classList.toggle('green')
	} else {
		dv.classList.toggle('try')
	}

} else if (today === text) {
	dv.classList.toggle('yellow')
} else if (today < text) {
	dv.classList.toggle('green')

}

if (checkedValue == "True") {
	checked.innerText = "Yes"
} else if (checkedValue === "False") {
	checked.innerText = "NO"
}