# Github has issues with img links, so we do this

blocks = [
	['src="grass.png"', 'src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABkAAAAZCAIAAABLixI0AAABhGlDQ1BJQ0MgcHJvZmlsZQAAKJF9kT1Iw1AUhU/TaqW0ONhBxCFDdbKLijjWKhShQqgVWnUweekfNGlJUlwcBdeCgz+LVQcXZ10dXAVB8AfE2cFJ0UVKvC8ptIjxwuN9nHfP4b37AKFVZZoZSACabhmZVFLM5VfF4Ct8CCCCEPplZtbnJCkNz/q6p26quzjP8u77syJqwWSATyROsLphEW8Qz2xadc77xFFWllXic+IJgy5I/Mh1xeU3ziWHBZ4ZNbKZeeIosVjqYaWHWdnQiKeJY6qmU76Qc1nlvMVZqzZY5578heGCvrLMdVqjSGERS5AgQkEDFVRhIU67ToqJDJ0nPfwjjl8il0KuChg5FlCDBtnxg//B79maxalJNymcBPpebPtjDAjuAu2mbX8f23b7BPA/A1d6119rAbOfpDe7WuwIGNwGLq67mrIHXO4Aw0912ZAdyU9LKBaB9zP6pjwwdAuE1ty5dc5x+gBkaVbpG+DgEBgvUfa6x7sHeuf2b09nfj/ynnJzZxCTdQAAAAlwSFlzAAAuIwAALiMBeKU/dgAAAAd0SU1FB+gBBA0PKD40qs4AAALSSURBVDjLTdTrbtpIGAbgx/YYjDknaZOsVO0l7IXubVbbNA2ngMEGG/aHmarWyD9Gmu/wnpJ//mXNkTnPJGwJfGXJO/+BJRfeaViwYMyFipojQ8E3pqwI5AwpKRhzZs0nYx5ISTkwpuTMGwdaGoJg7H5+8kHJX4zAijUnRgwp6MCJI1v2cYKUs+A7X5mwZsOBhJKWmgkZQ1Zk1NxAzYnAIwuOHATvBJ6YULHng4yEJc/UnNnScIuXRxJa5iwZMxGc+M6ejJw5HTVXkNPQciMn44kZmLEhoWHMs6Dkg18sWfKNG+9UtHyy4cySKYE0lp5y4xdrFj2PBWhJKZlx4hZh7pc9U5GQsuNGcn8v48yKq2DImAFLHiJ9Ky6MCQSurNhyi4UyrrzGcgdOvSa+cWJMwZ4fd+1pog5/c1e7dtKcUbzsaNiTC2pKanbknOgiOwk7Mh4YULGR1kxZ8kpOS8uVUrDj4v5PyZhS8oWUggsFOQcyKhY8seBKRkpO8Rv7mj0Nj7ywJNCS0FGRkzDm+gczfbOSrvfQPMJ8iQPndJyiICoOBJaMoiWTaG9RlXm/4y3u1ZCxpuMSrX6JGKcR8oQRGQ0nWkrGvR8L/mbOkR0rKm488xC3C3xhQU3DjIKKc7REKagYMmXCmY4zJ5o43YBF1H3KNWYGKgY80bITPPHKiA1v0S4D1lE4M2Z0rDhRUTCnYc2QCR9Ugle+krHnQM6CkhtnHu64WrG/y1XBIfJbktKRCV4oImUdS164xUkzWrb8iOHRkvFJwYBrrJsKGhLeODLlKWrqtxn6mK7Jo1z6IJjxSB01HAQ/KTkS4jpvVKQERrQMGDGLWu3bP1Lyi45Rr4k+EvpnE65s2DOMBpjHhOhJyLmQMGB3TwhFP9cngRcWjNiTMolq7BM9ZR0tMWDg/m3ZcuDCRbh3K2LgfdIxZcCWDY/RT2fGTDlG1LoIwoWj/wGVcyka+SexvgAAAABJRU5ErkJggg=="'],
	['src="dirt.png"', 'src="data:image/png;base64,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HBEvnadLjaXJ2ogM6pIht9S4wZ9w+ulOCNLE+wrokarMRxjs1NCmvpjfgLCzWaMRx4Fo1e9udBr7/Js+Ydyj1CrUP+R0PVpt0qN3WbrJnMlVH5miAD5kuOotrFC5jMSGWojF+BxMQi5yLGlb+IxWQqYKCXXDLwG9/Nkq30pZ4S1HkOy2j1t4Ny4YvB9f3UcltS/CiX0FqwShBNb2ynKT2wLx7tvsyu2fv7put+BSVCHadxk87u6flT2RhY6CUpCwkxa0MsSLvXl7T9d6kWE3pJYizivuGr/z1l5AgFshJiWUoAwPrXME/CPvQg253lNXvJ2ZisCFS8r40Fmgx88Ai04MeoFo/azveOr84snFYCLYQesznH75q4jFxbDiw92nw04F/tCauNYK207f+HXyzulzG5lQkHaQUn3Bk41O23XEsf3N5CkTPKnGkSQnlMgxnNnf/k7UWmf3fo+yGWrNdXwT2evu4I4lthccr8JJMbYMloUZy0feU3LQQhIokZ0Hz3+INtbsQzO888fZsUrGzsS6h8KE7ua6H3IAjhCD8G+91om5i96t/+RWmjk5ziOZyZYONAg9GMdMyBkdNCdD6fNv85Rtwfuz2CPj/d4dizG/v1N1L2R/NghNApYAAXKN1m1FkRF/xsQNHhW8K3vXWuNA6of40MgLAeHJCdFryfqxJ5LtNLkb4QGZNHh/EDiLyQdZmrC/e6EdLVvhVQPLGZOs8HaQ7jwX6ft9Kt3Vp4yZMCZ/79aY6jzEIc72oQpMzNQbnjwS2kVibFyM/b2/nKsgKFr765Ke/hu6yrshBfLwQFBxqxfzIXKD1iM0O8gwbHXC3y2520w6f//H2j911sIrEOyGW9m4pDy3yy3qOBYFCkHootu0/9rHY+ZpaqZ9/eWl/rQM+yxEh+j3hTZVu1w9OcICjAKr8t93/oOK8J6Pj0Cmjl+3/309sKG6YWvKeyBvZXWY/m8GOvk/wxEkGVdA6j4AAAAZdEVYdENvbW1lbnQAQ3JlYXRlZCB3aXRoIEdJTVBXgQ4XAAAAJXRFWHRkYXRlOmNyZWF0ZQAyMDI0LTAxLTA2VDIxOjQzOjM0KzAwOjAwyZjqFwAAACV0RVh0ZGF0ZTptb2RpZnkAMjAyNC0wMS0wNlQyMTo0MzozNCswMDowMLjFUqsAAAAodEVYdGRhdGU6dGltZXN0YW1wADIwMjQtMDEtMDlUMTM6MTk6MjkrMDA6MDC2D9kLAAAAG3RFWHRpY2M6Y29weXJpZ2h0AFB1YmxpYyBEb21haW62kTFbAAAAInRFWHRpY2M6ZGVzY3JpcHRpb24AR0lNUCBidWlsdC1pbiBzUkdCTGdBEwAAABV0RVh0aWNjOm1hbnVmYWN0dXJlcgBHSU1QTJ6QygAAAA50RVh0aWNjOm1vZGVsAHNSR0JbYElDAAAAAElFTkSuQmCC"'],
	['src="cobble.png"', 'src="data:image/png;base64,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"']
]




html = open("raw.svg", "r").read()
for src, to in blocks:
	html=html.replace(src, to)
f = open("out.svg", "w")
f.write(html)
f.close()
