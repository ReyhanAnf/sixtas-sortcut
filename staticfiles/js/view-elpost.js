function view_answer(post_id){
  const get_element_answer = document.getElementById("answer-" + post_id);
  const get_button_view = document.getElementById("answer-view-" + post_id);

  if(get_element_answer.classList.contains("hidden")){
    get_element_answer.classList.remove('hidden');
    get_element_answer.classList.add('block');
    get_button_view.innerHTML = 'close';
  }else if(get_element_answer.classList.contains("block")){
    get_element_answer.classList.remove('block');
    get_element_answer.classList.add('hidden');
    get_button_view.innerHTML = 'view';
  }
}


function view_reply(answer_id){
  const get_element_reply = document.getElementById("reply-" + answer_id);
  const get_button_view = document.getElementById("reply-view-" + answer_id);

  if(get_element_reply.classList.contains("hidden")){
    get_element_reply.classList.remove('hidden');
    get_element_reply.classList.add('block');
    get_button_view.innerHTML = 'close';
  }else if(get_element_reply.classList.contains("block")){
    get_element_reply.classList.remove('block');
    get_element_reply.classList.add('hidden');
    get_button_view.innerHTML = 'view';
  }
}



const actualBtn = document.getElementById('dropzone-files');

const fileChosen = document.getElementById('file-chosen');

actualBtn.addEventListener('change', function(){
  fileChosen.innerHTML += `<li
  class="w-full border-b-2 border-neutral-100 border-opacity-100 py-4 dark:border-opacity-50">
  ${this.files[0].name}
</li>`;

alert(this.file.name)
})