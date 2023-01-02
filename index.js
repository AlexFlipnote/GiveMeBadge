const get = (selector, scope = document) => scope.querySelector(selector);
const getAll = (selector, scope = document) => scope.querySelectorAll(selector);

const topNav = get('.menu');
const icon = get('.toggle');
const btns = getAll('.js-btn');

// typewriter effect
if (document.getElementById('demo')) {
  let i = 0;
  // TODO: Add Color
  const txt = `python index.py
            ⠀⠀⠀⠀⠀cclloooooooooooooo.
            ,;;;:oooooooooooooooooooooo.
            ;;;;ooooookKXKoooNMMWxooooo:..
            ;;;;ooooooXMMNooooXNK0xdddddoo
            ;;;;loookNMMWxoooodxxxxxxxxxxxxxo
            ;;;;ldkXXXXKdddddxxxxxxxxxxxxxxxx
            ;;lxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
            ;;xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
            ;;xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
            ;;xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
            ;;xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
            ;;xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
            ldxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

            Hey, welcome to the active developer badge bot.
            Please enter your bot's token below to continue.

            Don't close this application after entering the token
            You may close it after the bot has been invited and the command has been ran

            > `;
  const speed = 5;

  function typeItOut() {
    if (i < txt.length) {
      document.getElementById('demo').innerHTML += txt.charAt(i);
      i++;
      setTimeout(typeItOut, speed);
    }
  }

  setTimeout(typeItOut, 1800);
}

// toggle tabs on codeblock
const tabContainers = getAll('.tab-container');

// bind click event to each tab container
for (let i = 0; i < tabContainers.length; i++) {
  get('.tab-menu', tabContainers[i]).onclick = tabClick;
}

function tabClick(event) {
  const scope = event.currentTarget.parentNode;
  const clickedTab = event.target;
  const tabs = getAll('.tab', scope);
  const panes = getAll('.tab-pane', scope);
  const activePane = get(`.${clickedTab.getAttribute('data-tab')}`, scope);

  // remove all active tab classes
  for (let i = 0; i < tabs.length; i++) {
    tabs[i].classList.remove('active');
  }

  // remove all active pane classes
  for (let i = 0; i < panes.length; i++) {
    panes[i].classList.remove('active');
  }

  // apply active classes on desired tab and pane
  clickedTab.classList.add('active');
  activePane.classList.add('active');
}

function showNav() {
  if (topNav.className === 'menu') {
    topNav.className += ' responsive';
    icon.className += ' open';
  } else {
    topNav.className = 'menu';
    icon.classList.remove('open');
  }
}
icon.onclick = showNav;

function setActiveLink(event) {
  for (let i = 0; i < btns.length; i++) {
    btns[i].classList.remove('selected');
  }

  event.target.classList.add('selected');
}

function smoothScrollTo(i, event) {
  setActiveLink(event);

  window.scrollTo({
    behavior: 'smooth',
    top: sections[i].offsetTop - 20,
    left: 0
  });
}

if (btns.length && sections.length) {
  for (let i = 0; i < btns.length; i++) {
    btns[i].onclick = smoothScrollTo.bind(this, i);
  }
}

// fix menu to page-top once user starts scrolling
window.onscroll = () => {
  const docNav = get('.doc-nav > ul');

  if (docNav) {
    if (window.pageYOffset > 63) {
      docNav.classList.add('fixed');
    } else {
      docNav.classList.remove('fixed');
    }
  }
};