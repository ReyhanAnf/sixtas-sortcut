document.querySelector("#predform").reset();


let div_transit = document.querySelector(".transit");
let divT = document.querySelector(".content-scrape");
let text = document.querySelector("#raw-scrape").value;


text = text.replace("[" , "");
text = text.replace("]" , "");
text = text.split("</p>, ");

function typingwriter(element, text, j = 0){
  element.innerHTML += text[j];

  if(j < text.length){
    setTimeout(()=> typingwriter(element, text, j + 1), 4)
  }

  return;
}

function typingp(element, transit, text, i = 0){
  if(text[i] != "undefined"){
    transit.innerHTML = `${text[i]}`;
    transit_data = transit.textContent;
    typingwriter(element, transit_data);
  }



  if(i !== text.length - 1){
    setTimeout(()=> {
      element.innerHTML += `<br /> <br />`
      typingp(element, transit, text, i + 1)
    }, 6 * transit_data.length)
  }


}


typingp(divT, div_transit, text)

