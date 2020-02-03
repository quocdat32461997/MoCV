import setuptools

with open("README.md") as fh:
	long_description = fh.read()
	
setuptools.setup(
	name = "MoCV",
	version = "0.1.0",
	author = "datqngo",
	author_email = "quocdat32461997@yahoo.com",
	description = "List and details of Computer Vision algorithms",
	long_description = long_description,
	long_description_content_type = "text/markdown",
	url = "https://github.com/quocdat32461997/MoCV",
	packages = setuptools.find_packages(),
	classifiers = [
		"Programming Language :: Python :: 3",
        	"License :: OSI Approved :: MIT License",
        	"Operating System :: OS Independent",],
	install_requires = [
		"numpy",
		"matplotlib",
		"opencv-python"],
)
