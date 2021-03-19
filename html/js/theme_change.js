document.getElementById('light').onclick = function () { 
    document.getElementById('theme').classList.remove('dark');
    document.getElementById('theme').classList.add('light');
};


document.getElementById('dark').onclick = function () { 
    document.getElementById('theme').classList.remove('light');
    document.getElementById('theme').classList.add('dark');
};
