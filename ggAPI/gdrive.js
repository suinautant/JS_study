function getApi() {
  const dataSourceKey = "1IMxjsR6qU4xMk-OLHUJR8zZsPXKzLOoks-VfDl-P4_w";
  const dataSourceUrl = "https://docs.google.com/spreadsheets/d/" + dataSourceKey;
  var query = new google.visualization.Query(dataSourceUrl);
  query.setQuery('select *')
}

function init() {
  console.log(getApi());
  // getQeury();
}

init();