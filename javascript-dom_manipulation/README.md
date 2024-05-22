# JavaScript DOM Manipulation

## Description

This project focuses on learning and mastering DOM (Document Object Model) manipulation using JavaScript. You will learn how to select and modify HTML elements, handle events, and make asynchronous requests using the Fetch API. By completing this project, you will gain a solid understanding of how to dynamically interact with and update the content of web pages.

## Learning Objectives

By the end of this project, you should be able to:

- Select HTML elements using JavaScript.
- Understand the differences between ID, class, and tag name selectors.
- Modify the style of HTML elements.
- Get and update the content of HTML elements.
- Manipulate the DOM to add, remove, or modify elements.
- Make HTTP requests using `XmlHTTPRequest` and the Fetch API.
- Listen and bind to DOM events.
- Listen and bind to user events.

## Requirements

- All your files will be interpreted on Chrome browser (version 57.0 or later).
- All your files should end with a new line.
- A mandatory `README.md` file with meaningful information about the project must be placed at the root of the project folder.
- Your code should be semistandard compliant.
- You are not allowed to use `var`; use `let` or `const` instead.
- HTML should not reload for each action: DOM manipulation, update values, fetch data…

## Setup

To get started with this project, follow these steps:

1. Clone the repository to your local machine:
    ```bash
    git clone https://github.com/your-username/holbertonschool-higher_level_programming.git
    cd holbertonschool-higher_level_programming/javascript-dom_manipulation
    ```

2. Open the HTML files in your web browser to test the JavaScript scripts. For example, to test `0-script.js`:
    ```bash
    open 0-main.html
    ```

## Tasks

### Task 0: Color Me
Write a JavaScript script that updates the text color of the header element to red (`#FF0000`).

### Task 1: Click and turn red
Write a JavaScript script that updates the text color of the header element to red (`#FF0000`) when the user clicks on the tag with id `red_header`.

### Task 2: Add `.red` class
Write a JavaScript script that adds the class `red` to the header element when the user clicks on the tag with id `red_header`.

### Task 3: Toggle classes
Write a JavaScript script that toggles the class of the header element when the user clicks on the tag with id `toggle_header`.

### Task 4: List of elements
Write a JavaScript script that adds a `li` element to a list when the user clicks on the element with id `add_item`.

### Task 5: Change the text
Write a JavaScript script that updates the text of the header element to `New Header!!!` when the user clicks on the element with id `update_header`.

### Task 6: Star Wars character
Write a JavaScript script that fetches the character name from this URL: `https://swapi-api.hbtn.io/api/people/5/?format=json` and displays it in the HTML tag with id `character`.

### Task 7: Star Wars movies
Write a JavaScript script that fetches and lists the title for all movies by using this URL: `https://swapi-api.hbtn.io/api/films/?format=json`.

### Task 8: Say Hello!
Write a JavaScript script that fetches from `https://hellosalut.stefanbohacek.dev/?lang=fr` and displays the value of `hello` from that fetch in the HTML element with id `hello`.

## Resources

- [What is JavaScript?](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Introduction)
- [Introduction to the DOM](https://developer.mozilla.org/en-US/docs/Web/API/Document_Object_Model/Introduction)
- [Document Interface](https://developer.mozilla.org/en-US/docs/Web/API/Document)
- [Element Class](https://developer.mozilla.org/en-US/docs/Web/API/Element)
- [Locating DOM elements using selectors](https://developer.mozilla.org/en-US/docs/Web/API/Document/querySelector)
- [CSS Selectors](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Selectors)
- [Client-side Web APIs](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Client-side_web_APIs)
- [Manipulating documents](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Client-side_web_APIs/Manipulating_documents)
- [Fetching data from the server](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Client-side_web_APIs/Fetching_data)
- [What went wrong? Troubleshooting JavaScript](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/First_steps/What_went_wrong)

Happy coding!
