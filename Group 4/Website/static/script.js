// error handling...
const form = document.getElementById('beamForm');

form.addEventListener('submit', e => {
	e.preventDefault();

	const numSupports = form['numSupports'].value;
	const numJoints = form['numJoints'].value;
	const numSpans = form['numSpans'].value;

	if (numSupports === '') {
		addErrorTo('numSupports', 'Number of supports is required');
	} else {
		removeErrorFrom('numSpans');
	}

	if (numJoints === '') {
		addErrorTo('numJoints', 'Number of Joints is required');
	} else {
		removeErrorFrom('numJoints');
	}

	if (numSpans === '') {
		addErrorTo('numSpans', 'Number of Spans is required');
	} else {
		removeErrorFrom('numSpans');
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

