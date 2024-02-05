
#%%
import importlib
import scraping_economic
importlib.reload(scraping_economic)


# %%
from scraping_economic import download_jnto
download_jnto("../../save_dir/since2003_visitor_arrivals_December_2023.xlsx")

# %%
from scraping_economic import download_esri_di
download_esri_di("../../save_dir/景気動向指数.xlsx")
# %%
