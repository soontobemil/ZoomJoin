import os

vega_url = (
    ""
)
vega2_url = (
    ""
)
vancouver_url = (
    ""
)


while True:
    select_zoom = input(
        " #1 to join 🪐Vega Zoom \n #2 to join 🇨🇦 Vancouver Zoom \n : "
    ).strip()
    if select_zoom.lower() in ["1"]:
        os.system(f"open '{vega_url}' -a 'zoom.us.app'")
        break
    elif select_zoom.lower() in ["2"]:
        os.system(f"open '{vancouver_url }' -a 'zoom.us.app'")
        break
    else:
        print("Invalid Choice. Please enter either '1' or '2'.")

# webbrowser.open_new(url)

# https://vshn.zoom.us/j/84645966457?pwd=V0I0R2VTVnNkbzBxeDV4RGdQYktGdz09
