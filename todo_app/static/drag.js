function handleDragStart(e) {
  e.srcElement.style.opacity = "0.4";
  e.dataTransfer.setData("draggedElementId", e.srcElement.id)
  columns = document.getElementsByClassName("list_column")
  for (let column of columns) {
    column.classList.remove('drag_target_hidden')
    column.classList.add('drag_target')
  };
}

function handleDragEnd(e) {
  e.srcElement.style.opacity = "1";
  columns = document.getElementsByClassName("list_column")
  for (let column of columns) {
    column.classList.remove('drag_target')
    column.classList.add('drag_target_hidden')
  };
}
function handleDragOver(e) {
  e.preventDefault();
  return false;
}

function handleDrop(e) {
  e.stopPropagation(); // stops the browser from redirecting.

  itemId = e.dataTransfer.getData("draggedElementId")
  let dropList = e.target.classList.contains("list_column") ? e.target.id : e.target.parentElement.id;

  location.href = `/${dropList}/${itemId}`;
  return false;
}
