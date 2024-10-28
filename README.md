# <div align="center" style="font-size: 3em;">SpeakUp2.0 - Multimodal Lab</div>

## <div align="center" style="font-size: 2em; font-style: italic;">Code Repository for the (1) Setup (2) Preprocessing and (3) Analysis of Multimodal Signals</div>

<p align="center">
  <img src="https://github.com/user-attachments/assets/bc5daf90-a0f7-4d74-95e7-178647a844bc" alt="image" width="50%">
</p>

![Recording Setup](https://github.com/user-attachments/assets/6a710556-70a2-4fdf-b4e6-85c6a012ae84)

<p>This repository provides the complete codebase for the multimodal measurement framework used to capture, preprocess, and analyze subtle avoidance behaviors in live exposure therapy (ET) sessions. The code is organized into three main sections covering setup, preprocessing, and data analysis.</p>

<hr>

<h2>1. Multimodal Recording Setup</h2>
<p>This section includes all scripts needed to set up and record synchronized multimodal data streams from different equipment using Lab Streaming Layer (LSL). Here, we collect real-time data from the following devices:</p>
<ul>
    <li><strong>3 Synced Video Recoridngs
    <li><strong>Microphone:
    <li><strong>Balance Board:
    <li><strong>Eye Tracking
    <li><strong>Physiological Sensors (ECG and EDA)
 
   
    
</ul>
<p>Each script configures and manages the integration of these devices with LSL for synchronized recording.</p>

<h2>2. Preprocessing of Multimodal Signals</h2>
<p>This section contains scripts to preprocess and synchronize the collected multimodal data, ensuring alignment and format consistency across datasets. Key processes include:</p>
<ul>
    <li><strong>XDF Extraction:</strong> Converts raw data into XDF format for compatibility with further analysis steps.</li>
    <li><strong>Audio-Video Alignment:</strong> Synchronizes audio with video data, ensuring speech patterns are accurately paired with body movements.</li>
    <li><strong>Eye-Tracking Synchronization:</strong> Aligns gaze data with other data streams, providing precise temporal pairing for eye-tracking measurements.</li>

  
</ul>

<h2>3. Data Analysis</h2>
<p>This section includes scripts to quantify and analyze subtle avoidance metrics across each recorded modality:</p>
<ul>
    <li><strong>Quantification of Movements:</strong> Processes motion capture data to calculate frequency, duration, and extent of body movements.</li>
    <li><strong>Speech Patterns Analysis:</strong> Analyzes vocal metrics, including volume, frequency, and extended silences, to identify speech patterns associated with SABs.</li>
    <li><strong>Balance Board (CoP) Analysis:</strong> Computes CoP metrics from balance board data, quantifying postural sway and interpersonal distance.</li>
    <li><strong>Eye-Tracking Gaze Avoidance:</strong> Measures the duration and frequency of gaze fixations, particularly toward audience members, to assess gaze avoidance.</li>
    <li><strong>Physiology (Heart Rate and Skin Conductance):</strong> Calculates heart rate and tonic skin conductance values, providing a physiological profile of arousal during exposure.</li>
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
