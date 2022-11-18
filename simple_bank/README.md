A simple Bank program created with the concept of Object Oriented Programming (OOP)
<br>
<ul>
    <li><b>User Class</b> is created to initialize the user when the user runs the program.
        <ul><li>It consists of a constructer to intiliaze the user's name, age, and gender</li><li>It also contains of a function to display the user data </li>
        </ul>
    </li>
    <li><b>Bank Class</b> is created to perform different operations: deposit, withdraw, view balance. It inhertis the <b>User Class</b>.
        <ul><li>It consists of a constructer to intiliaze user balance to 0 and also contains a super() method</li><li>It also contains of a functions to deposit money, withdraw money and view balance </li>
        </ul>
    </li>
</ul>
<br>
The user after entering his/her name, age and gender is prompted to select one of the 4 options to proccess further:
<ol>
    <li>View your details</li>
    <li>Deposit Money</li>
    <li>Withdraw Money</li>
    <li>View Balance</li>
</ol>