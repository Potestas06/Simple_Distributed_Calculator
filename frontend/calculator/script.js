const socket = new WebSocket("ws://localhost:8000");

let keys = document.querySelectorAll("#calc span");
let operators = ["+", "-", "x", "÷"];
let decimalAdded = false;

for (let i = 0; i < keys.length; i++) {
  keys[i].onclick = function (e) {
    let lastChar;
    const input = document.querySelector(".display");
    const inputVal = input.innerHTML;
    const btnVal = this.innerHTML;

    if (btnVal === "C") {
      input.innerHTML = "";
      decimalAdded = false;
    } else if (btnVal === "=") {
      let equation = inputVal;
      lastChar = equation[equation.length - 1];

      equation = equation.replace(/x/g, "*").replace(/÷/g, "/");

      if (operators.indexOf(lastChar) > -1 || lastChar === ".") {
        equation = equation.replace(/.$/, "");
      }

      if (equation) {
        //input.innerHTML = eval(equation);
        const message = {
          work: equation,
        };
        socket.send(JSON.stringify(message));

        socket.onmessage = (event) => {
          input.innerHTML = event.data;
        };
      }

      decimalAdded = false;
    } else if (operators.indexOf(btnVal) > -1) {
      lastChar = inputVal[inputVal.length - 1];

      if (inputVal !== "" && operators.indexOf(lastChar) === -1)
        input.innerHTML += btnVal;
      else if (inputVal === "" && btnVal === "-") input.innerHTML += btnVal;

      if (operators.indexOf(lastChar) > -1 && inputVal.length > 1) {
        input.innerHTML = inputVal.replace(/.$/, btnVal);
      }
      decimalAdded = false;
    } else if (btnVal === ".") {
      if (!decimalAdded) {
        input.innerHTML += btnVal;
        decimalAdded = true;
      }
    } else if (btnVal === "␡") {
      input.innerHTML = input.innerHTML.slice(0, -1);
      decimalAdded = false;
    } else {
      input.innerHTML += btnVal;
    }

    // prevent page jumps
    e.preventDefault();
  };
}

const toggleSwitch = document.querySelector(
  '.theme-switch input[type="checkbox"]'
);

function switchTheme(e) {
  if (e.target.checked) {
    document.documentElement.setAttribute("data-theme", "dark");
  } else {
    document.documentElement.setAttribute("data-theme", "light");
  }
}

toggleSwitch.addEventListener("change", switchTheme, false);

socket.onclose = function () {
  const input = document.querySelector(".display");
  input.innerHTML = " lost connection to server";
};
