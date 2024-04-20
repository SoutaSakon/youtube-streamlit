import streamlit as st # type: ignore
import numpy as np # type: ignore
import pandas as pd # type: ignore

st.title('Streamlit 超入門')
st.write('DateFrame')

df = pd.DataFrame(
    np.random.randn(10, 2) / [150, 150] + [34.698897206302654, 135.5300151598336],
    columns=['lat', 'lon'])
st.map(df)

# st.dataframe(df.style.highlight_max(axis=0), width=200, height=200)
col1, col2, col3 = st.columns(3)
col1.metric("Temperature", "70 °F", "1.2 °F")
col2.metric("Wind", "9 mph", "-8%")
col3.metric("Humidity", "86%", "4%")

"""
# 章
## 節
### 項

```python
import streamlit as st
import numpy as np
import pandas as pd
```

"""