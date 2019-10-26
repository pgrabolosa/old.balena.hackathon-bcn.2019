## `raw/joystick`

Expected values:

    - `"up"`
    - `"down"`
    - `"left"`
    - `"right"`
    - `"middle"`

## `disp/#`

Expected values, in JSON, two formats:

  - `{"color": [R, G, B]}` where R, G, B are 0-255 values
  - `{"image": [[R, G, B] * 64]}` where R, G, B are 0-255 values
  - `{"text": string}` which will call the sense hat library `show_message` function (banner style)
  + optionnally, may be `{"text": string, "text_color": [R, G, B]}`  to specify the text color 
