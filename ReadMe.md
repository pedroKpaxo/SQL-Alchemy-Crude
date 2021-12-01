# SQL Alchemy To-Do

An implementation of a SQL Alchemy using tkinter.
Based on a MVC pattern design.

- [Install](#Install)
- [Usage](#Usage)


## Install

Make sure that you have the SQL Alchemy installed.
It is the only required package.

```sh
pip install SQLAlchemy
```

## Usage
This app follows an MVC design pattern, and everything is packed accordingly.

The main.py file is the 'entry point' for the application.
It imports everything from the Vegas Pack

- [Vegas_Model](#Model)
- [Vegas_View](#View)
- [Vegas_Control](#Control)


### Model

All the SQL logic, models and the database configurations are found here.
[Vegas Model](./Vegas_Pack/Vegas_Model)

### View

All the tkinter widgets and related code comes here.
I also created a separetd folder packing some low level widgets for usability.
[Vegas Model](./Vegas_Pack/Vegas_View)

### Control
The [Vegas_Control.py](./Vegas_Pack/Vegas_Control.py) packs all the code responsible for the main TK object and all the others funcions.




