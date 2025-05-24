function calculateBMI() {
    let weight = parseFloat(document.getElementById('weight').value);
    let height = parseFloat(document.getElementById('height').value);

    if (!weight || !height) {
        document.getElementById('bmi').textContent = "Please enter weight and height!";
        return;
    }

    height = height / 100;
    let bmi = weight / (height * height);
    bmi = bmi.toFixed(2);

    document.getElementById('bmi').textContent = "Your BMI is " + bmi;
}
