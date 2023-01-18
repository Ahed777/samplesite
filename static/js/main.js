function dateChanger() {
	const date = Date(Date.now().toString());
	const dateElement = document.getElementById("date");
	dateElement.innerHTML = date;
}
dateChanger();
