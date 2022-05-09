# Customized-Calendar
Users can add, delete, modify, and search for the events they created in the GUI
![image](https://user-images.githubusercontent.com/89577799/167335469-d17a9fae-d4cc-44aa-bcde-8d871bd006c7.png)
## Tutorial of this customized calendar
<details open="open">
  <summary><b>Table of Contents</b></summary>
  <ol>
    <li>
      <a href="#introduction">Introduction</a>
      <ul> 
    </li>
      </ul>
    <li>
      <a href="#the-model">The Model</a>
      <ul>
        <li><a href="#python-and-gurobi-implementation">Python and Gurobi Implementation</a></li>
        <li><a href="#parameter-setting">Parameter Setting</a></li>
        <li><a href="#the-classical-newsvendor-model-with-consumption">The Classical Newsvendor Model with Consumption</a></li>
        <li><a href="#the-newsvendor-model-with-barter-exchange">The Newsvendor Model with Barter Exchange</a></li>
        <ul>
          <li><a href="#the-newsvendor-model-with-barter-exchange-demand-uncertainty">The Newsvendor Model with Barter Exchange: Demand uncertainty</a></li>
        </ul>
      </ul>
    </li>
    <li><a href="#visualization">Visualization</a></li>
    <li><a href="#conclusion">Conclusion</a></li>
  </ol>
</details>

# __Introduction__
This repository is a tutorial for the Customized Calendar using python.
# __The Model__
* We consider the `single-period` inventory (newsvendor) problem with barter exchange from the retailer's perspective, in which the customer's demand is `stochastic` and characterized by a `random variable`. The retailer determines the optimal stocking policy to satisfy the customer demand at the beginning of the selling season.  
* Suppose the retailer purchases only a single product A from the supplier, and the retail price is set by the supplier or the market. This problem is to decide the optimal order quantity to `maximize its own expected profit`.  
* The retailer orders `Q units of the product A` from the supplier at a `fixed price` at the beginning of the selling season, then it sells product A to its customers at the `retail price`.  
