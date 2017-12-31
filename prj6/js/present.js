function openPresent(event) {
  const image = event.currentTarget;
  const title = document.querySelector('h1');
  if (Math.floor(Math.random() * 10) > 3) {
  		image.src = 'images/giphy.gif';
  		title.textContent = 'Hooray- You were nice!';
  	} else {
  		image.src = 'images/coal.jpg'
  		title.textContent = 'Sorry - you get coal!';
  	}

  
 
  
  image.removeEventListener('click', openPresent);
}

const image = document.querySelector('img');
image.addEventListener('click', openPresent);
