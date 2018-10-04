# Using AWS X-Ray Ex10
X-Ray analyse the application and gives back the inforamtion.

### start RDS instance

### the code
`ex-xray.zip`

* import X-Ray Libraries
```python
from aws_xray_sdk.core import xray_recorder, patch_all
from aws_xray_sdk.ext.flask.middleware import XRayMiddleware
```

* decorator: `@xray_recorder.capture()`


### Xray deamon
[Xray daemon documentation](https://docs.aws.amazon.com/xray/latest/devguide/xray-daemon.html)
* copy the download link (Linux(executable)-aws-xray-daemon-linux-2.x.zip (sig))
* `wget <the link>` in `~` directory
* unzip
* run by `./xray`

### see diagnostics information
* open X-Ray dashboard
* service map , traces


### annotation
add searchable annotations to the trace segment
```python
from aws_xray_sdk.core import xray_recorder
...
document = xray_recorder.current_segment()
```


### stop RDS instance
