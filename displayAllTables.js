            // Select all elements with the class name "htmlCalendarMonth"
            var elements = document.querySelectorAll(".htmlCalendarMonth");

            // Now 'elements' is a NodeList containing all elements with the specified class name
            // You can loop through the NodeList to access each element
            for (var i = 0; i < elements.length; i++) {
                elements[i].style.display = "block"
            }