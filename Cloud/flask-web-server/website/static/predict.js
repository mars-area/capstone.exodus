async function run() {
    const model = await tf.automl.loadImageClassification('model.json');
    const image = document.getElementById('get_prediction');
    const predictions = await model.classify(image);
    const dataPrediction = predictions;
    const fruit1 = dataPrediction[0];
    const fruit2 = dataPrediction[1];
    const fruit3 = dataPrediction[2];
    //for debuging
    //console.log(dataPrediction);
    //console.log('buah1: ' + JSON.stringify(fruit1, null, 2));
    //console.log('buah2: ' + fruit2);
    //console.log('buah3: ' + fruit3);
    //console.log('label: ' + fruit1.label)
    //console.log('prob: ' + fruit1.prob)
    // Show the resulting object on the page.
    const result = document.querySelector('.container')
    const pre = document.createElement('pre');
    // Insert class
    pre.className += 'container result';
    // condition
    if( fruit1.prob > fruit2.prob && fruit1.prob > fruit3.prob ) {
        const hasil = fruit1.prob * 100;
        console.log('I believe ' + hasil + '% ' + 'This is a ' + fruit1.label);
        pre.innerHTML = 'I believe ' + hasil.toFixed(2) + '% ' + 'This is ' + fruit1.label
    }
    else if( fruit2.prob > fruit1.prob && fruit2.prob > fruit3.prob ) {
        const hasil = fruit2.prob * 100;
        console.log('I believe ' + hasil + '% ' + 'This is a ' + fruit2.label);
        pre.innerHTML = 'I believe ' + hasil.toFixed(2) + '% ' + 'This is ' + fruit2.label
    }
    else {
        const hasil = fruit3.prob * 100;
        console.log('I believe ' + hasil + '% ' + 'This is a ' + fruit3.label);
        pre.innerHTML = 'I believe ' + hasil.toFixed(2) + '% ' + 'This is ' + fruit3.label
    }
    result.append(pre);
    alert('prediksi selesai');
    return dataPrediction
}