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
<p>Working in progress...</p>

<h2>Dependencies</h2>
<p>Refer to the <code>requirements.txt</code> file for a complete list of dependencies. Installation of required packages can be done using:</p>

<pre><code>pip install -r requirements.txt</code></pre>

<h2>License and Citation</h2>

<hr>

</body>
</html>
