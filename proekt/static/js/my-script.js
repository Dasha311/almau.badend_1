$(document).ready(function() {
    // Обработчик клика на первую кнопку
    $('#switch1').on('click', function() {
      $('.loginMsg').toggleClass("visibility"); // Переключает класс видимости сообщения о входе
      $('.frontbox').addClass("moving"); // Добавляет класс для движения переднего блока
      $('.signupMsg').toggleClass("visibility"); // Переключает класс видимости сообщения о регистрации
  
      $('.signup').toggleClass('hide'); // Переключает класс скрытия/отображения формы регистрации
      $('.login').toggleClass('hide'); // Переключает класс скрытия/отображения формы входа
    });
  
    // Обработчик клика на вторую кнопку
    $('#switch2').on('click', function() {
      $('.loginMsg').toggleClass("visibility"); // Переключает класс видимости сообщения о входе
      $('.frontbox').removeClass("moving"); // Убирает класс движения переднего блока
      $('.signupMsg').toggleClass("visibility"); // Переключает класс видимости сообщения о регистрации
  
      $('.signup').toggleClass('hide'); // Переключает класс скрытия/отображения формы регистрации
      $('.login').toggleClass('hide'); // Переключает класс скрытия/отображения формы входа
    });
  
    // Выполнить клик на первую кнопку через 1 секунду
    setTimeout(function() {
      $('#switch1').click()
    }, 1000);
  
    // Выполнить клик на вторую кнопку через 3 секунды
    setTimeout(function() {
      $('#switch2').click()
    }, 3000);
  });
  