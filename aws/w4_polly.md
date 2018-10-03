# Exercise - Polly
Polly for text-to-speech

### polly from aws CLI
from Cloud9:
* `aws polly help`
* `aws polly synthesize-speech` : to create synthesized speech
    * mandatory parameters:
        * `--output-format <value>`
        * `--text <value>`
        * `--voice-id <value>`
        * `outfile <value>`
    * for help: `aws polly synthesize-speech help`
    * example:
        * `aws polly synthesize-speech --output-format mp3 --text 'Any text you want' --voice-id Matthew output.mp3`
* `aws polly descibe-voices`

### add pollyReadOnly access
* IAM dashboard
* Users
* add permissions
* attach existing policies directly
* AmazonPollyReadOnlyAccess


### to implement voice to app
```python
import io
from flask import send_file
polly = boto3.client("polly")
message = "hello such such"
resoponse = polly.synthesize_speech(VoiceId='Nicole', Text=message, OutputFormat='mp3')
polly_bytes = response['AudioStream'].read()
return send_file(
    io.BytesIO(polly_bytes),
    mimetype='audio/mpeg',
    cache_timeout=-1
)
```

### edit HTML
from
```HTML
<li><p class="navbar-text">Hello, {{current_user.nickname}}!</p></li>
```
to
```HTML
<li><p class="navbar-text">Hello, {{current_user.nickname}}!
<span class="glyphicon glyphicon-volume-up" style="cursor: pointer;" onclick="document.getElementById('audio').load();document.getElementById('audio').play();"></span>
<audio id="audio">
  <source src="{{ url_for('members_voice') }}" type="audio/mpeg">
</audio></p>
</li>
```
