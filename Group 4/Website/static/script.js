const form = document.getElementById('form');

form.addEventListener('submit', e => {
	e.preventDefault();

	const typeofbeam = form['typeofbeam'].value;
	const reactions = form['reactions'].value;
	const supports = form['supports'].value;
	const moments = form['moments'].value;

	if (typeofbeam === '') {
		addErrorTo('typeofbeam', 'Type of Beam is required');
	} else {
		removeErrorFrom('typeofbeam');
	}

	if (reactions === '') {
		addErrorTo('reactions', 'Number of Reactions is required');
	} else {
		removeErrorFrom('reactions');
	}

	if (supports === '') {
		addErrorTo('supports', 'Number of Supports is required');
	} else if (!isValid(supports)) {
		addErrorTo('supports', 'Number of Supports is not valid');
	} else {
		removeErrorFrom('supports');
	}

	if (moments === '') {
		addErrorTo('moments', 'Moments is required');
	} else {
		removeErrorFrom('moments');
	}
});

function addErrorTo(field, message) {
	const formControl = form[field].parentNode;
	formControl.classList.add('error');

	const small = formControl.querySelector('small');
	small.innerText = message;
}

function removeErrorFrom(field) {
	const formControl = form[field].parentNode;
	formControl.classList.remove('error');
}

