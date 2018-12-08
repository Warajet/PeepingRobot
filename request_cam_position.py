from selenium import webdriver

# create a driver
driver = webdriver.Chrome()

ip = "192.168.0.118"
# get the homepage
driver.get("http://" + ip + "/piviewer")

y_element = driver.find_element_by_id("y")
z_element = driver.find_element_by_id("z")


print(y_element)
print(z_element)
