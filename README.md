# <div align="center" style="font-size: 3em;">SpeakUp2.0 - Multimodal Lab</div>

## <div align="center" style="font-size: 2em; font-style: italic;">Code Repository for the (1) Setup (2) Preprocessing and (3) Analysis of Multimodal Signals</div>

<p align="center">
  <img src="https://github.com/user-attachments/assets/bc5daf90-a0f7-4d74-95e7-178647a844bc" alt="image" width="50%">
</p>

![Recording Setup](https://github.com/user-attachments/assets/6a710556-70a2-4fdf-b4e6-85c6a012ae84)

<p>This repository provides the scripts for used in the SpeakUp2.0 Multimodal Labroatory used record, preprocess, and analyze subtle avoidance behaviors during a live exposure therapy (ET) sessions. 
  The code is organized into three main sections: setup, preprocessing, and data analysis.</p>

<hr>

<h2>1. Multimodal Recording Setup</h2>
<p>This section includes all the scripts needed to set up and record synchronized multimodal data streams from different equipment using the Lab Streaming Layer (LSL). In our setup, we used the following devices:</p>
<ul>
    <li><strong>3 Synced Video Recordings</strong></li>
    <li><strong>Microphone</strong></li>
    <li><strong>Balance Board</strong></li>
    <li><strong>Eye Tracking</strong></li>
    <li><strong>Physiological Sensors (ECG and EDA)</strong></li>
</ul>
<p>You can see more information about each piece of equipment (specs, prices, links, etc.) in the <strong>Multimodal Lab Equipment List.xlsx</strong>.</p>


<h2>2. Preprocessing of Multimodal Signals</h2>
<p>This section contains scripts to preprocess the multimodal streams from the XDF unitary files (obtained from LSL), the raw videos and the raw eye tracking. This secton consists of:</p>
<ul>
    <li><strong>1_XDF_PROCESSING:</strong> Extract relevant data streams from XDF and convert it into a workable format (e.g., csv or wav).</li>
    <li><strong>2_AUDIO_VIDEO_SYNC:</strong> Clipping the raw videos based on LSL times and synchronizing them with the relevant audios.</li>
    <li><strong>3_PUPIL_CLOUD_EYE TRACKING SYNC</strong> Synchronizing the LSL eye tracking data with the Pupil Cloud Eye tracking uploads.</li>

    ![Preprocessing overview](https://github.com/user-attachments/assets/dcd88c8d-bf64-4ed8-9d21-e698834e9a1f)


  
</ul>

<h2>3. Data Analysis</h2>
<p>This section includes scripts to quantify and analyze subtle avoidance metrics across each recorded modality:</p>
<ul>
    <li><strong>Quantification of Movements:</strong> Processes motion capture data to calculate frequency, duration, and extent of body movements.</li>
    <li><strong>Speech Patterns Analysis:</strong> Analyzes vocal metrics, including volume, frequency, and extended silences, to identify relevant speech patterns.</li>
    <li><strong>Balance Board (CoP) Analysis:</strong> Computes Centre of Pressure metrics from balance board data, quantifying postural sway and interpersonal distance from the audience.</li>
    <li><strong>Eye-Tracking Gaze Avoidance:</strong> Measures the duration and frequency of gaze fixations, particularly toward audience members, to assess gaze avoidance.</li>
    <li><strong>Physiology (Heart Rate and Skin Conductance):</strong> Calculates heart rate and tonic skin conductance values from the ECG and EDA signals.</li>
</ul>

<hr>

<h2>Getting Started</h2>

<h3> (1) Using ANACONDA (Beginner Friendly)</h3>
<p>This method sets up the repository using <strong>Anaconda</strong> https://www.anaconda.com/download . This option is better for beginners or for managing dependencies in isolated virtual environments.</p> <p> You can comprehensive information on how to do this (alongside a user-friendly video) in the envision box "Getting Started" page: https://envisionbox.org/gettingstarted.html </p>

<h4>Step 1: Install Anaconda</h4>
<p>
To get started, download and install Anaconda from the official <a href="https://www.anaconda.com/products/distribution">Anaconda website</a>. This installation includes Python, pip, and Jupyter Notebook, as well as the ability to create virtual environments.
</p>

<p>For more detailed installation instructions:</p>
<ul>
    <li><strong>Windows:</strong> Follow the guide <a href="https://docs.anaconda.com/anaconda/install/windows/">here</a>.</li>
    <li><strong>MacOS/Linux:</strong> Follow the guide <a href="https://docs.anaconda.com/anaconda/install/linux/">here</a>.</li>
</ul>

<h4>Step 2: Install Git</h4>
<p>Git is needed to clone the repository. Install Git by following the instructions:</p>
<ul>
    <li><strong>Windows:</strong> Use <a href="https://git-scm.com/">this guide</a> to install Git.</li>
    <li><strong>MacOS/Linux:</strong> Git is often pre-installed. If not, follow <a href="https://git-scm.com/">this guide</a>.</li>
</ul>

<h4>Step 3: Clone the Repository</h4>
<p>Open your terminal (or Anaconda Prompt on Windows) and navigate to the folder where you want to save the repository. Then run:</p>
<pre><code>git clone https://github.com/DavAhm/SpeakUp2.0-Multimodal-Setup-Preprocessing-Analysis.git
</code></pre>

<h4>Step 4: Set Up the Environment</h4>
<p>Create a virtual environment to isolate the project’s dependencies. First, navigate to the directory where you cloded in the GitHub Repository and then run the following commands in your terminal:</p>
<pre><code>conda create --name myenv python=3.9
conda activate myenv
conda install pip
</code></pre>

<h4>Step 5: Install Dependencies</h4>
<p>Navigate to the project folder and install the required dependencies (i.e., the required libraries and packages to run the scripts):</p>
<pre><code>pip install -r requirements.txt
</code></pre>

<h4>Step 6: Run Jupyter Notebook</h4>
<p>Start Jupyter Notebook in the project folder to explore the scripts:</p>
<pre><code>jupyter notebook
</code></pre>

<h4>Step 6a: Run Jupyter Notebook in Visual Studio code</h4>
<p>Alternatively, you can simply open each notebook in Visual Studio code and run in there using the Anaconda virtual environment as the intepreter following these instructions: https://docs.anaconda.com/working-with-conda/ide-tutorials/vscode/</p>

<p>Open any <code>.ipynb</code> file in Jupyter Notebook to begin working with the repository.</p>


<h3>(2) Using PIP  (Advanced and Lightweight)</h3>
<p>This method sets up the repository using <strong>pip</strong> and the standard Python tools to create a virtual environment. This method is faster and more lightweight than Anaconda but assumes some familiarity with Python and terminal commands.</p>

<h4>Step 1: Install Python and Pip</h4>
<p>Make sure you have Python 3.9+ and pip installed on your system:</p>
<ul>
    <li><strong>Windows:</strong> Download Python from the official <a href="https://www.python.org/downloads/">Python website</a> and follow the installation instructions. Ensure you check the box to "Add Python to PATH" during installation.</li>
    <li><strong>MacOS/Linux:</strong> Python is often pre-installed. Check your version using the command:
        <pre><code>python3 --version</code></pre>
        If needed, download Python from the <a href="https://www.python.org/downloads/">Python website</a>.
    </li>
</ul>

<h4>Step 2: Install Git</h4>
<p>Git is needed to clone the repository. Install Git by following these instructions:</p>
<ul>
    <li><strong>Windows:</strong> Use <a href="https://git-scm.com/">this guide</a> to install Git.</li>
    <li><strong>MacOS/Linux:</strong> Git is often pre-installed. If not, follow <a href="https://git-scm.com/">this guide</a>.</li>
</ul>

<h4>Step 3: Clone the Repository</h4>
<p>Open your terminal and navigate to the folder where you want to save the repository. Then run:</p>
<pre><code>git clone https://github.com/DavAhm/SpeakUp2.0-Multimodal-Setup-Preprocessing-Analysis.git
cd SpeakUp2.0-Multimodal-Setup-Preprocessing-Analysis
</code></pre>

<h4>Step 4: Create a Virtual Environment</h4>
<p>Create a virtual environment to isolate the project’s dependencies. In your terminal, run:</p>
<pre><code>python3 -m venv myenv
</code></pre>
<p>Activate the virtual environment:</p>
<ul>
    <li><strong>Windows:</strong>
        <pre><code>myenv\Scripts\activate</code></pre>
    </li>
    <li><strong>MacOS/Linux:</strong>
        <pre><code>source myenv/bin/activate</code></pre>
    </li>
</ul>

<h4>Step 5: Install Dependencies</h4>
<p>With the virtual environment activated, install the required dependencies for the project:</p>
<pre><code>pip install -r requirements.txt
</code></pre>

<h4>Step 6: Run Jupyter Notebook</h4>
<p>Start Jupyter Notebook in the project folder to explore the scripts:</p>
<pre><code>jupyter notebook
</code></pre>

<p>Open any <code>.ipynb</code> file in Jupyter Notebook to begin working with the repository.</p>

<h4>Step 6a: Run Jupyter Notebook in Visual Studio Code</h4>
<p>Alternatively, you can open and run the Jupyter Notebook files in Visual Studio Code by following these instructions: <a href="https://code.visualstudio.com/docs/datascience/jupyter-notebooks">VS Code Jupyter Setup Guide</a>.</p>


<h3>Troubleshooting</h3>
<p>If you encounter any issues:</p>
<ul>
    <li>Make sure all dependencies are installed correctly by re-running <code>pip install -r requirements.txt</code>.</li>
    <li>Check that your Python version is 3.9 or higher.</li>
    <li>Ensure Jupyter Notebook is installed and properly configured.</li>
    <li>Refer to the <a href="https://github.com/DavAhm/SpeakUp2.0-Multimodal-Setup-Preprocessing-Analysis/issues">Issues</a> page for common problems.</li>
</ul>

<h2>Dependencies</h2>
<p>Refer to the <code>requirements.txt</code> file for a complete list of dependencies. Installation of required packages can be done using:</p>

<pre><code>pip install -r requirements.txt</code></pre>

<p>Alèternatively, you can install each required packages individually inside your envirornment <p>
<pre><code>conda install "name of library"</code></pre>
or
<pre><code>pip install "name of library" </code></pre>


<h2>Citations</h2>
<small>
    <p><strong>Author:</strong> Davide Ahmar</p>
    <p><strong>Contact:</strong> ahmar.davide@gmail.com</p>
    <p><strong>Code Contributors:</strong></p>
    <ul>
        <li>Wim Pouw: wim.pouw@donders.ru.nl</li>
        <li>Sarka Kadava: sarka.kadava@ru.nl</li>
    </ul>
</small>


<hr>

</body>
</html>
