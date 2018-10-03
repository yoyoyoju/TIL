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

