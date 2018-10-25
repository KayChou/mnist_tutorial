from sklearn.datasets import fetch_mldata

# download and read mnist
print("begin download...")
mnist = fetch_mldata('MNIST original', data_home='./')
print("Download finish")