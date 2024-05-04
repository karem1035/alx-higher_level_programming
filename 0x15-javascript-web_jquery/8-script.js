$.get(
  'https://swapi-api.alx-tools.com/api/films/?format=json',
  function (data) {
    const arr = data.results;
    for (let i = 0; i < arr.length; i++) {
      $('UL#list_movies').append(`<li>${arr[i].title}</li>`);
    }
  }
);
