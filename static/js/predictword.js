document.querySelector("#predform").reset();


let div_transit = document.querySelector(".transit");
let divT = document.querySelector(".content-scrape");
let text = document.querySelector("#raw-scrape").value;
let text_scan = document.querySelector("#text-scan");
let process_pred = document.querySelector("#process-pred");
let percent_pred = document.querySelector(".predict-percent");
process_pred.scrollIntoView();


text = text.replace("[" , "");
text = text.replace("]" , "");
text = text.split("</p>, ");


function typingwriter(element, text, j = 0){
  element.innerHTML += text[j];

  if(j < text.length){
    setTimeout(()=> typingwriter(element, text, j + 1), 3)
  }

  return;
}

function typingp(element, transit, text, i = 0){
  if(text[i] != "undefined"){
    transit.innerHTML = `${text[i]}`;
    transit_data = transit.textContent;
    typingwriter(element, transit_data);
  }

  if(text.length == 1){
    text_scan.textContent = "Done..";
    let a = setTimeout(()=>{
      process_pred.classList.add("hidden")
      percent_pred.classList.remove("hidden")
      clearTimeout(a)
      return;
    }, 3000)
  }

  if(i == Math.floor(text.length / 5 * 1 )){
    text_scan.textContent = "Vectorizing"
  }else if (i == Math.floor(text.length / 5 * 2) - 3){
    text_scan.textContent = "Predict"
  }else if (i == Math.floor(text.length / 5 * 3) - 2){
    text_scan.textContent = "Done.."
  }else if (i == Math.floor(text.length / 5 * 4) - 1){
    process_pred.classList.add("hidden")
    percent_pred.classList.remove("hidden")
  }else if (i == text.length) {
    process_pred.classList.add("hidden")
    percent_pred.classList.remove("hidden")
  }

  if(i !== text.length - 1){
    setTimeout(()=> {
      
      element.innerHTML += `<br /> <br />`
      typingp(element, transit, text, i + 1)
    }, 5 * transit_data.length)
  }


}


typingp(divT, div_transit, text)

// =======================================CHART======================

let ctx = document.getElementById("chart").getContext("2d");
let val = document.querySelector("#score").value
val = Number(val);

let chart = new Chart(ctx, {
  type: "doughnut",
  data: {
    labels: ['Fake', 'Real'],
    datasets: [
      {
        label:  "Predict",
        data: [val, 100-val],
        backgroundColor: ["#ed4a4a", "#09b88c"],
      }
    ]
  },
  options: {
    responsive: true,
    plugins: {
      legend: {
        position: 'top',
      },
      title: {
        display: true,
        text: 'Result'
      }
    }
  },
});
